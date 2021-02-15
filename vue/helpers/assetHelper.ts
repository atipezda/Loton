export function getAsset(assetName: string):string{

  const asset = !assetName || assetName === '' ? 'placeholder.png' : assetName
  return require('@/assets/' + asset + '')
}
